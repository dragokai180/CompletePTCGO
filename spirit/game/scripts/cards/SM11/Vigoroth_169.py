from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='40773024-db11-5aa1-864d-fb8db8eb6324',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name',
    display_name='Vigoroth',
    searchable_by=['Vigoroth', 'Stage 1', 'Vigoroth'],
    subtypes=['Stage 1'],
    collector_number=169,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Slakoth.Name',
    family_id=287,
    abilities=[
        Attack(
            title='Roar',
            game_text='Your opponent switches their Active Pokémon with 1 of their Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Slash',
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)
