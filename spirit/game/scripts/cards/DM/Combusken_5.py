from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='135f43ff-5609-500f-9c95-0fdae5e3d5c1',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name',
    display_name='Combusken',
    searchable_by=['Combusken', 'Stage 1', 'Combusken'],
    subtypes=['Stage 1'],
    collector_number=5,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Torchic.Name',
    family_id=255,
    abilities=[
        Ability(
            title='Natural Cure',
            game_text='Whenever you attach an Energy card from your hand to this Pokémon, remove all Special Conditions from it.',
            passive=standard_passive('Whenever you attach an Energy card from your hand to this Pokémon, remove all Special Conditions from it.'),
        ),
        Attack(
            title='Lunge',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
