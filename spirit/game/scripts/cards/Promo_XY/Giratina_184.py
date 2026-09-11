from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='34c29038-3972-54d1-99d0-c44a1c2258e2',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Giratina.Name',
    display_name='Giratina',
    searchable_by=['Giratina', 'Basic', 'Giratina'],
    subtypes=['Basic'],
    collector_number=184,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=487,
    abilities=[
        Ability(
            title='Devour Light',
            game_text='Each Pokémon BREAK has no Abilities (this includes Abilities of its previous Evolution).',
            passive=standard_passive('Each Pokémon BREAK has no Abilities (this includes Abilities of its previous Evolution).'),
        ),
        Attack(
            title='Shadow Claw',
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
