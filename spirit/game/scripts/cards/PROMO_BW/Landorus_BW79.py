from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import blazing_claws, dark_clamp, leech_life, solar_transporter
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="1050987c-0559-5708-8451-817f87eb27b9",
    key="PROMO_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Landorus.Name",
    display_name="Landorus",
    searchable_by=["Landorus","Basic","Landorus","Team Plasma"],
    subtypes=["Basic","Team Plasma"],
    collector_number=79,
    set_code="PROMO_BW",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    abilities=[
        Attack(
            title="Extrasensory",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 30 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Rock Tomb",
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=dark_clamp,
        ),
    ],
)
