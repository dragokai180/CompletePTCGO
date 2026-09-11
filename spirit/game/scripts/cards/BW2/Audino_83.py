from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="86f05f3f-b8bf-5172-8a8d-70d73850d7e2",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Audino.Name",
    display_name="Audino",
    searchable_by=["Audino","Basic","Audino"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Powerful Slap",
            game_text="Flip a coin for each Energy attached to this Pokémon. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Heal Pulse",
            game_text="Heal 50 damage from 1 of your Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=bw_legacy_attack,
        ),
    ],
)
