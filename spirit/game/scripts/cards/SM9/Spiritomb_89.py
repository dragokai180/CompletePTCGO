from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1df63159-b445-5e30-8634-2f284739a8be',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name',
    display_name='Spiritomb',
    searchable_by=['Spiritomb', 'Basic', 'Spiritomb'],
    subtypes=['Basic'],
    collector_number=89,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=442,
    abilities=[
        Attack(
            title='Spirit Compressor',
            game_text='Search your deck for up to 4 Pokémon and discard them. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Spooky Shot',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
