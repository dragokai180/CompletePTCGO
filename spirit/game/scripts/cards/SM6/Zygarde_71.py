from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b60037e7-5ddf-5ac5-a84d-5584c9e79514',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zygarde.Name',
    display_name='Zygarde',
    searchable_by=['Zygarde', 'Basic', 'Zygarde'],
    subtypes=['Basic'],
    collector_number=71,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=718,
    abilities=[
        Ability(
            title='Earthen Aura',
            game_text="Damage from this Pokémon's attacks isn't affected by Weakness or Resistance.",
            passive=standard_passive("Damage from this Pokémon's attacks isn't affected by Weakness or Resistance."),
        ),
        Attack(
            title='Peace Maker',
            game_text='If your opponent has an Ultra Beast in play, this attack does 30 more damage.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
