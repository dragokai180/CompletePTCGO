from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.session.passives import Passive, effective_pokemon_types


def _other_player(carrier):
    playmat = carrier.parent.parent if carrier.parent else None
    return next(
        (
            child.owning_player_id for child in (playmat.children if playmat else [])
            if child.owning_player_id
            and child.owning_player_id != carrier.owning_player_id
        ),
        None,
    )


def _darkness_side(carrier):
    return _other_player(carrier) \
        if carrier.get_attribute(AttrID.CARD_ORIENTATION, 0) == 1 \
        else carrier.owning_player_id


class ReverseValleyPassive(Passive):
    """Normal: owner's Darkness +10; opponent's Metal takes 10 less."""

    def modify_damage_dealt(self, calc, carrier):
        if not calc.is_attack or not calc.is_opposing or calc.attacker is None:
            return
        if calc.attacker.owning_player_id != _darkness_side(carrier):
            return
        if PokemonTypes.DARKNESS.value in effective_pokemon_types(
            calc.board, calc.attacker
        ):
            calc.amount += 10

    def modify_damage_taken(self, calc, carrier):
        if not calc.is_attack or not calc.is_opposing:
            return
        metal_side = _other_player(carrier) \
            if _darkness_side(carrier) == carrier.owning_player_id \
            else carrier.owning_player_id
        if calc.target.owning_player_id != metal_side:
            return
        if PokemonTypes.METAL.value in effective_pokemon_types(
            calc.board, calc.target
        ):
            calc.amount = max(0, calc.amount - 10)


card = StadiumCardDef(
    guid='4243938d-79db-5a5e-889c-d38432a88f37',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ReverseValley.Name',
    display_name='Reverse Valley',
    searchable_by=['Reverse Valley', 'Stadium', 'ReverseValley'],
    subtypes=['Stadium'],
    collector_number=110,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=ReverseValleyPassive(),
    orientation_choices=[
        (
            "Orientação normal",
            "Seus Pokémon Noturnos causam +10; os Pokémon Metálicos adversários recebem -10.",
        ),
        (
            "Orientação invertida",
            "Seus Pokémon Metálicos recebem -10; os Pokémon Noturnos adversários causam +10.",
        ),
    ],
    allows_same_name_replacement=True,
)
