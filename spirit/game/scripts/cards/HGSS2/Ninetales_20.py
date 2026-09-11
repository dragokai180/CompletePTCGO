from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='97f5978b-1433-5e5e-b02d-6da755727e83',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name',
    display_name='Ninetales',
    searchable_by=['Ninetales', 'Stage 1', 'Ninetales'],
    subtypes=['Stage 1'],
    collector_number=20,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name',
    family_id=37,
    abilities=[
        Attack(
            title='Heat Acceleration',
            game_text='Search your discard pile for up to 3 Fire Energy cards and attach them to 1 of your Pokémon.',
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Searing Flame',
            game_text='The Defending Pokémon is now Burned.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
