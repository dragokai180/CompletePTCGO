from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='40790c45-5b3c-58fa-a131-d470782ed923',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rhydon.Name',
    display_name='Rhydon',
    searchable_by=['Rhydon', 'Stage 1', 'Rhydon'],
    subtypes=['Stage 1'],
    collector_number=66,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rhyhorn.Name',
    family_id=111,
    abilities=[
        Attack(
            title='Rock Tumble',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=standard_attack,
        ),
        Attack(
            title='Megahorn',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
