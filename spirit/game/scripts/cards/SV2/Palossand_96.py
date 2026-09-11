from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='75f535b3-b044-5117-9feb-3c1a6fd6d00d',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Palossand.Name',
    display_name='Palossand',
    searchable_by=['Palossand', 'Stage 1', 'Palossand'],
    subtypes=['Stage 1'],
    collector_number=96,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sandygast.Name',
    family_id=769,
    abilities=[
        Attack(
            title='Spooky Shot',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title='Earthen Power',
            game_text='If you have a Stadium in play, this attack does 80 more damage.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
