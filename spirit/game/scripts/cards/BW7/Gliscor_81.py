from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import switch_self_attack
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="5a04e26b-d2b3-5aac-b044-5e2d8efa1bfd",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gliscor.Name",
    display_name="Gliscor",
    searchable_by=["Gliscor","Stage 1","Gliscor"],
    subtypes=["Stage 1"],
    collector_number=81,
    set_code="BW7",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name",
    abilities=[
        Attack(
            title="Poison Ring",
            game_text="The Defending Pokémon is now Poisoned. The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Night Slash",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=switch_self_attack(),
        ),
    ],
)
