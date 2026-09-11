from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ce06c856-5998-5c98-bf90-9f9b02114cb7',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mudsdale.Name',
    display_name='Mudsdale',
    searchable_by=['Mudsdale', 'Stage 1', 'Mudsdale'],
    subtypes=['Stage 1'],
    collector_number=20,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Mudbray.Name',
    family_id=750,
    abilities=[
        Attack(
            title='Enhanced Stomp',
            game_text='If this Pokémon has a Pokémon Tool card attached to it, this attack does 60 more damage.',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='High Horsepower',
            game_text='This Pokémon does 40 damage to itself.',
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=standard_attack,
        ),
    ],
)
