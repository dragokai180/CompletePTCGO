from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='36355701-69d0-515b-90cc-2125f06b3242',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMarowak.Name',
    display_name='Alolan Marowak',
    searchable_by=['Alolan Marowak', 'Stage 1', 'AlolanMarowak'],
    subtypes=['Stage 1'],
    collector_number=12,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name',
    family_id=104,
    abilities=[
        Attack(
            title='Limbo Limbo',
            game_text='Search your deck for up to 2 basic Energy cards and attach them to your Pokémon in any way you like. Then, shuffle your deck.',
            cost={},
            effect=standard_attack,
        ),
        Attack(
            title='Alolan Club',
            game_text='This attack does 20 damage for each of your Pokémon in play that has Alolan in its name.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
