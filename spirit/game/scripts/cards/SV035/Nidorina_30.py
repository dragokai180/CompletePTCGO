from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='355617ff-7ea5-5d93-8c25-292df8893ef7',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name',
    display_name='Nidorina',
    searchable_by=['Nidorina', 'Stage 1', 'Nidorina'],
    subtypes=['Stage 1'],
    collector_number=30,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name',
    family_id=29,
    abilities=[
        Attack(
            title='Fetch Family',
            game_text='Search your deck for up to 3 Pokémon, reveal them, and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Sharp Fang',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
