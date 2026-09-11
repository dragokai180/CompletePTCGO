from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='274dde60-f147-5ff6-8a63-ebc1e5b0f749',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.NsResolve.Name',
    display_name="N's Resolve",
    searchable_by=["N's Resolve", 'Supporter', 'NsResolve'],
    subtypes=['Supporter'],
    collector_number=200,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Discard the top 6 cards of your deck. If any of those cards are basic Energy cards, attach them to 1 of your Benched Dragon Pokémon.'),
    condition=standard_trainer_condition('Discard the top 6 cards of your deck. If any of those cards are basic Energy cards, attach them to 1 of your Benched Dragon Pokémon.'),
)
