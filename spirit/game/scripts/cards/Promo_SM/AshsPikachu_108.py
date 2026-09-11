from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e6223265-774b-5e2b-9b79-bae4c6603b86',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AshsPikachu.Name',
    display_name="Ash's Pikachu",
    searchable_by=["Ash's Pikachu", 'Basic', 'AshsPikachu'],
    subtypes=['Basic'],
    collector_number=108,
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
            title='I Choose You!',
            game_text='Search your deck for a Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Thunderbolt',
            game_text='Discard all Energy from this Pokémon.',
            cost={PokemonTypes.LIGHTNING: 3},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
