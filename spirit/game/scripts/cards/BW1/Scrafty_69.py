from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="27c8a96a-641f-5779-85ee-9cc23a200cc2",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scrafty.Name",
    display_name="Scrafty",
    searchable_by=["Scrafty","Stage 1","Scrafty"],
    subtypes=["Stage 1"],
    collector_number=69,
    set_code="BW1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name",
    abilities=[
        Attack(
            title="Spit Acid",
            game_text="The Defending Pokémon is now Burned. Flip a coin. If heads, the Defending Pokémon is also Paralyzed.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            effect=bw_legacy_attack,
        ),
        Attack(
            title="High Jump Kick",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
