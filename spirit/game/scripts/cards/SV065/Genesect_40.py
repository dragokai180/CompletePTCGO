from spirit.game.data_utils import PokemonCardDef, Ability, Attack, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from spirit.game.session.passives import Passive
from spirit.game.session.passives import carrier_pokemon


GENESECT_GUID = "27f3b2fa-b010-4314-a4b4-0686d0913bbb"


def _has_pokemon_tool_attached(pokemon) -> bool:
    # Scan attachments under the Pokemon's stack for a Pokemon Tool.
    stack = list(getattr(pokemon, "children", []) or [])
    while stack:
        ent = stack.pop()
        if getattr(ent, "card_obj", None) is not None:
            trainer_type = ent.get_attribute(AttrID.TRAINER_TYPE, None)
            if trainer_type == TrainerType.POKEMON_TOOL.value:
                return True
        stack.extend(getattr(ent, "children", []) or [])
    return False


class _AceNullifierPassive(Passive):
    """If Genesect has a Pokémon Tool attached, block opponent's ACE SPEC."""

    def blocks_trainer_play(self, card, player_id: str, carrier) -> bool:
        # `player_id` is the player attempting to play the trainer card.
        holder = carrier_pokemon(carrier)
        if holder is None:
            return False
        if holder.owning_player_id == player_id:
            return False
        if not _has_pokemon_tool_attached(holder):
            return False
        definition = def_for(getattr(card, "archetype_id", None) or "")
        return "ACE SPEC" in (getattr(definition, "subtypes", None) or [])


card = PokemonCardDef(
    guid=GENESECT_GUID,
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Genesect.Name",
    display_name="Genesect",
    searchable_by=["Genesect", "Basic", "Genesect"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=649,
    abilities=[
        Ability(
            title="ACE Nullifier",
            game_text=(
                "If this Pokémon has a Pokémon Tool attached, your "
                "opponent can't play any ACE SPEC cards from their hand."
            ),
            passive=_AceNullifierPassive(),
        ),
        Attack(
            title="Magnetic Blast",
            game_text="",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)

