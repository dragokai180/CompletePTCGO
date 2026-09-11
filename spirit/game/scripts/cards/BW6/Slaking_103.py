from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_ability, bw_legacy_attack, bw_legacy_passive, bw_stadium_ability, bw_stadium_triggers, bw_tool_abilities, bw_trainer_effect, bw_trainer_passive

card = PokemonCardDef(
    guid="2fd74bde-49cd-5446-8e28-7e9622c4f0be",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slaking.Name",
    display_name="Slaking",
    searchable_by=["Slaking","Stage 2","Slaking"],
    subtypes=["Stage 2"],
    collector_number=103,
    set_code="BW6",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name",
    abilities=[
        Ability(
            title="Unobservant",
            game_text="If your opponent's Active Pokémon is a Basic Pokémon, this Pokémon can't attack.",
            passive=bw_legacy_passive("If your opponent's Active Pokémon is a Basic Pokémon, this Pokémon can't attack."),
        ),
        Attack(
            title="Crushing Blow",
            game_text="Discard an Energy attached to the Defending Pokémon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            effect=bw_legacy_attack,
        ),
    ],
)
