from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5d9aee42-f003-5af0-a299-9bdb78d774b1',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Persian.Name',
    display_name='Persian',
    searchable_by=['Persian', 'Stage 1', 'Persian'],
    subtypes=['Stage 1'],
    collector_number=182,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name',
    family_id=53,
    abilities=[
        Ability(
            title='Gathering of Cats',
            game_text='Ignore all Energy in the attack costs of each of your Pokémon in play that has the Caturday attack.',
            passive=standard_passive('Ignore all Energy in the attack costs of each of your Pokémon in play that has the Caturday attack.'),
        ),
        Attack(
            title='Claw Slash',
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)
