from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f50a07e6-3713-589d-8877-ceeb2328fd5e',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name',
    display_name='Togetic',
    searchable_by=['Togetic', 'Stage 1', 'Togetic'],
    subtypes=['Stage 1'],
    collector_number=137,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name',
    family_id=175,
    abilities=[
        Attack(
            title='Energy Present',
            game_text='Attach an Energy card from your hand to 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Magical Shot',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
