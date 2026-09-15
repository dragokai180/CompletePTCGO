from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations, Triggers
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.bw_era import bw_legacy_ability, bw_legacy_attack, bw_legacy_passive, bw_stadium_ability, bw_stadium_triggers, bw_tool_abilities, bw_trainer_effect, bw_trainer_passive
from spirit.game.card_effects.pokemon import top_entry
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card

card = PokemonCardDef(
    guid="3da2c124-e0ee-5885-85be-32854b5092ce",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krookodile.Name",
    display_name="Krookodile",
    searchable_by=["Krookodile","Stage 2","Krookodile"],
    subtypes=["Stage 2"],
    collector_number=62,
    set_code="BW2",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name",
    abilities=[
        Ability(
            title="Black Eyes",
            game_text="Once during your turn (before your attack), if this Pokémon is your Active Pokémon, you may flip a coin. If heads, discard an Energy attached to your opponent's Active Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            effect=bw_legacy_ability,
        ),
        Attack(
            title="Thrash",
            game_text="Flip a coin. If heads, this attack does 20 more damage. If tails, this Pokémon does 20 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
