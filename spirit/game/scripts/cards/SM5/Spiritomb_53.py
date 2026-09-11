from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3eb8b390-d51a-528e-8e01-4667ef815966',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name',
    display_name='Spiritomb',
    searchable_by=['Spiritomb', 'Basic', 'Spiritomb'],
    subtypes=['Basic'],
    collector_number=53,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=442,
    abilities=[
        Attack(
            title='Lightless World',
            game_text='Put 2 Supporter cards from your discard pile into your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Terrify',
            game_text="If the Defending Pokémon is a Basic Pokémon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
