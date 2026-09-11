from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='061ac64c-5ca1-57cb-a0af-610ad9b2f227',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vikavolt.Name',
    display_name='Vikavolt',
    searchable_by=['Vikavolt', 'Stage 2', 'Vikavolt'],
    subtypes=['Stage 2'],
    collector_number=208,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Charjabug.Name',
    family_id=738,
    abilities=[
        Ability(
            title='Stealthy Body',
            game_text='If there is any Stadium card in play, this Pokémon has no Weakness.',
            passive=standard_passive('If there is any Stadium card in play, this Pokémon has no Weakness.'),
        ),
        Attack(
            title='Electricannon',
            game_text='You may discard all Lightning Energy from this Pokémon. If you do, this attack does 100 more damage.',
            cost={PokemonTypes.LIGHTNING: 4},
            damage=120,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
