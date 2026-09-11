from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6fcccba5-6c74-5a8d-ad30-b61ebd49e33b',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AshsPikachu.Name',
    display_name="Ash's Pikachu",
    searchable_by=["Ash's Pikachu", 'Basic', 'AshsPikachu'],
    subtypes=['Basic'],
    collector_number=110,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=25,
    abilities=[
        Attack(
            title='Iron Tail',
            game_text='Flip a coin until you get tails. This attack does 20 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Thunder',
            game_text='Flip a coin. If tails, this Pokémon does 20 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
