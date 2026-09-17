from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, AttrID
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="8a2c8cea-36c4-5b14-b7f3-9470a41f2c77",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Serperior.Name",
    display_name="Serperior",
    searchable_by=["Serperior","Stage 2","Serperior"],
    subtypes=["Stage 2"],
    # Original client slots 116..140 hold Radiant Collection RC1..RC25.
    collector_number=118,
    attributes={AttrID.CARD_NUMBER_TEXT.value: {"type": "string", "value": "RC3"}},
    set_code="BW11",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Servine.Name",
    abilities=[
        Ability(
            title="Royal Garden",
            game_text="If this Pokémon has any Grass Energy attached to it, this Pokémon has no Retreat Cost.",
            passive=bw_legacy_passive("If this Pokémon has any Grass Energy attached to it, this Pokémon has no Retreat Cost."),
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
