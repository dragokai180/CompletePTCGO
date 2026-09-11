from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='21aba8e7-07ca-52df-b041-0991ef37309d',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bewear.Name',
    display_name='Bewear',
    searchable_by=['Bewear', 'Stage 1', 'Bewear'],
    subtypes=['Stage 1'],
    collector_number=49,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name',
    family_id=760,
    abilities=[
        Attack(
            title='Mix-Up',
            game_text="Flip a coin. If heads, discard the top 3 cards of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Tantrum',
            game_text='This Pokémon is now Confused.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
