from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bcb6dfe0-c1ab-54aa-8115-65b2b8df976c',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name',
    display_name='Bronzong',
    searchable_by=['Bronzong', 'Stage 1', 'Bronzong'],
    subtypes=['Stage 1'],
    collector_number=61,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name',
    family_id=436,
    abilities=[
        Ability(
            title='Metal Links',
            game_text='Once during your turn (before your attack), you may attach a Metal Energy card from your discard pile to 1 of your Benched Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Hammer In',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
