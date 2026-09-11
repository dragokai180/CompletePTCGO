from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8bb76b9b-52b9-57d0-bd5e-9044cdaf6a20',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Floette.Name',
    display_name='Floette',
    searchable_by=['Floette', 'Stage 1', 'Floette'],
    subtypes=['Stage 1'],
    collector_number=64,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Flabb.Name',
    family_id=669,
    abilities=[
        Ability(
            title='Flower Veil',
            game_text='Each of your Grass Pokémon in play gets +20 HP.',
            passive=standard_passive('Each of your Grass Pokémon in play gets +20 HP.'),
        ),
        Attack(
            title='Fairy Wind',
            cost={PokemonTypes.FAIRY: 1},
            damage=20,
        ),
    ],
)
