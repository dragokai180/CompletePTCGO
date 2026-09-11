from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='038d596b-ae25-517a-87e6-b77560e2737c',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name',
    display_name='Gabite',
    searchable_by=['Gabite', 'Stage 1', 'Gabite'],
    subtypes=['Stage 1'],
    collector_number=98,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gible.Name',
    family_id=443,
    abilities=[
        Attack(
            title='Ascension',
            game_text='Search your deck for a card that evolves from this Pokémon and put it onto this Pokémon to evolve it. Then, shuffle your deck.',
            cost={PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Slash',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
