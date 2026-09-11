from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c0b97e58-382a-5ad4-bc17-399a7c02657b',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name',
    display_name='Mewtwo',
    searchable_by=['Mewtwo', 'Basic', 'Mewtwo'],
    subtypes=['Basic'],
    collector_number=100,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=150,
    abilities=[
        Attack(
            title='Psy Bolt',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Zen Blade',
            game_text="This Pokémon can't use Zen Blade during your next turn.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
