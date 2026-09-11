from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fd3ec7ae-2b73-5eaf-bdae-aec7330a082e',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanVulpix.Name',
    display_name='Alolan Vulpix',
    searchable_by=['Alolan Vulpix', 'Basic', 'AlolanVulpix'],
    subtypes=['Basic'],
    collector_number=53,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=37,
    abilities=[
        Ability(
            title='Secret Alleyway',
            game_text='If you have any Fairy Pokémon in play, this Pokémon has no Retreat Cost.',
            passive=standard_passive('If you have any Fairy Pokémon in play, this Pokémon has no Retreat Cost.'),
        ),
        Attack(
            title='Gnaw',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
