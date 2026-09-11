from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2e3c23d8-07e6-5371-866d-e031c78cce54',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Electrode.Name',
    display_name='Electrode',
    searchable_by=['Electrode', 'Stage 1', 'Electrode'],
    subtypes=['Stage 1'],
    collector_number=39,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name',
    family_id=100,
    abilities=[
        Ability(
            title='Electro Shaker',
            game_text='When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may move any number of Lightning Energy from your Pokémon to your other Pokémon in any way you like.',
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Speed Ball',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
