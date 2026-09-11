from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6596d7ea-a4bd-5d7b-a8fc-e6f335b14623',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pyroar.Name',
    display_name='Pyroar',
    searchable_by=['Pyroar', 'Stage 1', 'Pyroar'],
    subtypes=['Stage 1'],
    collector_number=37,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name',
    family_id=667,
    abilities=[
        Attack(
            title='Swirling Inferno',
            game_text="Discard all Pokémon Tool cards and Special Energy from each of your opponent's Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=standard_attack,
        ),
        Attack(
            title='Heat Blast',
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=140,
        ),
    ],
)
