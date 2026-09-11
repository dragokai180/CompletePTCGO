from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f88dcd7c-de83-5ce0-b296-f2ea9da03329',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mimikyuex.Name',
    display_name='Mimikyu ex',
    searchable_by=['Mimikyu ex', 'Basic', 'ex', 'Mimikyuex'],
    subtypes=['Basic', 'ex'],
    collector_number=4,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=190,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=778,
    abilities=[
        Attack(
            title='Void Return',
            game_text='You may switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Energy Burst',
            game_text='This attack does 30 damage for each Energy attached to both Active Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
