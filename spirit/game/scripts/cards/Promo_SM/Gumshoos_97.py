from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2bcff3a3-22fc-50b3-b1b9-1efac60e01a3',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gumshoos.Name',
    display_name='Gumshoos',
    searchable_by=['Gumshoos', 'Stage 1', 'Gumshoos'],
    subtypes=['Stage 1'],
    collector_number=97,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Yungoos.Name',
    family_id=735,
    abilities=[
        Attack(
            title='Identify',
            game_text='Your opponent reveals their hand. If you find a Pokémon there, this attack does 80 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Whap Down',
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)
