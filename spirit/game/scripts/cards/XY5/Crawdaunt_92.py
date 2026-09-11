from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ee940f97-1bfd-55f8-ac29-694e97b1bcef',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Crawdaunt.Name',
    display_name='Crawdaunt',
    searchable_by=['Crawdaunt', 'Stage 1', 'Crawdaunt'],
    subtypes=['Stage 1'],
    collector_number=92,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Corphish.Name',
    family_id=341,
    abilities=[
        Ability(
            title='Unruly Claw',
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon, you may discard an Energy attached to your opponent's Active Pokémon.",
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Crabhammer',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
