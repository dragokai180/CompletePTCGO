from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="26b8018c-24c0-508f-a992-b67366f8c998",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Audino.Name",
    display_name="Audino",
    searchable_by=["Audino","Basic","Audino"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Wake-up Beam",
            game_text="Remove all Special Conditions from the Defending Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Drain Slap",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=heal_attack(30),
        ),
    ],
)
