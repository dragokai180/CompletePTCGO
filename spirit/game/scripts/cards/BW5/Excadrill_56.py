from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per, snipe_attack
from spirit.game.card_effects.support_common import recover_from_discard, requires_discard

card = PokemonCardDef(
    guid="1a4d8cc8-9918-56fb-9ecc-ffd58c696845",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Excadrill.Name",
    display_name="Excadrill",
    searchable_by=["Excadrill","Stage 1","Excadrill"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="BW5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name",
    abilities=[
        Attack(
            title="Tunnel Strike",
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1},
            effect=snipe_attack(30, pool="bench"),
        ),
        Attack(
            title="Dig Uppercut",
            game_text="Put a card from your discard pile into your hand.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
            effect=recover_from_discard(count=1, minimum=1, reveal=False, to="hand"),
        ),
    ],
)
