from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_ability, bw_legacy_attack, bw_legacy_passive, bw_stadium_ability, bw_stadium_triggers, bw_tool_abilities, bw_trainer_effect, bw_trainer_passive

card = PokemonCardDef(
    guid="71279cd3-037c-5af4-b564-093e1ac5761a",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stoutland.Name",
    display_name="Stoutland",
    searchable_by=["Stoutland","Stage 2","Stoutland"],
    subtypes=["Stage 2"],
    collector_number=122,
    set_code="BW7",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name",
    abilities=[
        Ability(
            title="Sentinel",
            game_text="As long as this Pokémon is your Active Pokémon, your opponent can't play any Supporter cards from his or her hand.",
            passive=bw_legacy_passive("As long as this Pokémon is your Active Pokémon, your opponent can't play any Supporter cards from his or her hand."),
        ),
        Attack(
            title="Wild Tackle",
            game_text="Flip a coin. If tails, this Pokémon does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            effect=bw_legacy_attack,
        ),
    ],
)
