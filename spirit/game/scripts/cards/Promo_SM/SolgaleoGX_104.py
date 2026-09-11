from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a7921108-dc5d-545a-8d3b-d63b3adc1198',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.SolgaleoGX.Name',
    display_name='Solgaleo-GX',
    searchable_by=['Solgaleo-GX', 'Stage 2', 'GX', 'SolgaleoGX'],
    subtypes=['Stage 2', 'GX'],
    collector_number=104,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=250,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name',
    family_id=791,
    abilities=[
        Ability(
            title='Shining Mane',
            game_text='Your Pokémon in play have no Weakness.',
            passive=standard_passive('Your Pokémon in play have no Weakness.'),
        ),
        Attack(
            title='Turbo Strike',
            game_text='Attach 2 basic Energy cards from your discard pile to 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
        Attack(
            title='Prominence-GX',
            game_text="Heal all damage from all of your Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
