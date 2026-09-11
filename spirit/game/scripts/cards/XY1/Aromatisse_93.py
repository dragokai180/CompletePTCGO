from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7bb23cd9-d13c-5697-ab1a-cc339c572665',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Aromatisse.Name',
    display_name='Aromatisse',
    searchable_by=['Aromatisse', 'Stage 1', 'Aromatisse'],
    subtypes=['Stage 1'],
    collector_number=93,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Spritzee.Name',
    family_id=682,
    abilities=[
        Ability(
            title='Fairy Transfer',
            game_text='As often as you like during your turn (before your attack), you may move a Fairy Energy attached to 1 of your Pokémon to another of your Pokémon.',
            effect=standard_ability,
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title='Fairy Wind',
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
