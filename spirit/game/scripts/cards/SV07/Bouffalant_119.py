from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import TakesLessPassive
from spirit.game.session.effects import is_basic_pokemon


def _is_bouffalant(pokemon):
    name = getattr(def_for(pokemon.archetype_id), "display_name", "") or ""
    return name == "Bouffalant"


def _basic_colorless_ally(target, carrier):
    if target.owning_player_id != carrier.owning_player_id:
        return False
    if not is_basic_pokemon(target):
        return False
    types = target.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.COLORLESS.value in types


class CurlyWallPassive(TakesLessPassive):
    """If another Bouffalant is in play, your Basic Colorless Pokémon take 60
    less damage from opposing attacks (after W/R). Does not stack."""

    def __init__(self):
        super().__init__(60, protects=_basic_colorless_ally, stack_key="CurlyWall")

    def modify_damage_taken(self, calc, carrier):
        owner = carrier.owning_player_id
        others = [
            p for p in calc.board.pokemon_in_play(owner)
            if p is not carrier and _is_bouffalant(p)
        ]
        if not others:
            return
        super().modify_damage_taken(calc, carrier)


card = PokemonCardDef(
    guid="c405a10a-8c62-5c25-8fea-0bde2263b6fb",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bouffalant.Name",
    display_name="Bouffalant",
    searchable_by=["Bouffalant","Basic","Bouffalant"],
    subtypes=["Basic"],
    collector_number=119,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    family_id=626,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Ability(
            title="Curly Wall",
            game_text="As long as you have at least 1 other Bouffalant in play, all of your Basic Colorless Pokémon take 60 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance). The effect of Curly Wall doesn't stack.",
            passive=CurlyWallPassive(),
        ),
        Attack(
            title="Boundless Power",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            locks_next_turn=True,
        ),
    ],
)
