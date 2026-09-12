from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_ability, bw_legacy_attack, bw_legacy_passive, bw_stadium_ability, bw_stadium_triggers, bw_tool_abilities, bw_trainer_effect, bw_trainer_passive

card = PokemonCardDef(
    guid="66d0897d-d420-5f9c-9d00-727e7773bb68",
    key="PROMO_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crobat.Name",
    display_name="Crobat",
    searchable_by=["Crobat","Stage 2","Crobat","Team Plasma"],
    subtypes=["Stage 2","Team Plasma"],
    collector_number=51,
    set_code="PROMO_BW",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name",
    abilities=[
        Ability(
            title="Night Sight",
            game_text="Once during your turn (before your attack), you may draw a card.",
            activation=Activations.ONCE_PER_TURN,
            effect=bw_legacy_ability,
        ),
        Attack(
            title="Ultra-Toxic Fang",
            game_text="The Defending Pokémon is now Poisoned. Put 4 damage counters instead of 1 on that Pokémon between turns.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=bw_legacy_attack,
        ),
    ],
)
