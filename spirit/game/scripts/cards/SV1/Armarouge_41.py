from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bfdcd24d-7dfb-5527-8447-ddacab96af06',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Armarouge.Name',
    display_name='Armarouge',
    searchable_by=['Armarouge', 'Stage 1', 'Armarouge'],
    subtypes=['Stage 1'],
    collector_number=41,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name',
    family_id=935,
    abilities=[
        Ability(
            title='Fire Off',
            game_text='As often as you like during your turn, you may move a Fire Energy from 1 of your Benched Pokémon to your Active Pokémon.',
            effect=standard_ability,
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title='Flame Cannon',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
