from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="538afe62-a391-5f27-8feb-75445511f0f4",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gothitelle.Name",
    display_name="Gothitelle",
    searchable_by=["Gothitelle","Stage 2","Gothitelle"],
    subtypes=["Stage 2"],
    collector_number=47,
    set_code="BW2",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gothorita.Name",
    abilities=[
        Ability(
            title="Magic Room",
            game_text="As long as this Pokémon is your Active Pokémon, your opponent can't play any Item cards from his or her hand.",
            passive=bw_legacy_passive("As long as this Pokémon is your Active Pokémon, your opponent can't play any Item cards from his or her hand."),
        ),
        Attack(
            title="Madkinesis",
            game_text="Does 20 more damage for each Psychic Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
