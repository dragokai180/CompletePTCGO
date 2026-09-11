from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6b6938c9-f9bd-5d76-a2f7-bab97c424adc',
    key='Promo_HGSS',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Meganium.Name',
    display_name='Meganium',
    searchable_by=['Meganium', 'Stage 2', 'Prime', 'Meganium'],
    subtypes=['Stage 2', 'Prime'],
    collector_number=8,
    set_code='Promo_HGSS',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'HGSS08'}},
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name',
    family_id=154,
    abilities=[
        Ability(
            title='Leaf Trans',
            game_text="As often as you like during your turn (before your attack), you may move a Grass Energy attached to 1 of your Pokémon to another of your Pokémon. This power can't be used if Meganium is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title='Solarbeam',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
